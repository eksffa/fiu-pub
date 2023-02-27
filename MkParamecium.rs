/* 
 Patrick Tracanelli
 Materials Science and Engineering MS
 FIU Department of Mechanical and Materials Engineering
 http://mme.fiu.edu
 Toy beings for a toy universe
 Synth a Paramecyum from the 87M sequence for Paramecium tetraurelia (ASM16542v1) 
 Format FASTA download from https://protists.ensembl.org/Paramecium_tetraurelia/Info/Index
*/

use std::f64::consts::PI;
use std::vec::Vec;
use std::fs;

struct Element {
    mass: f64,
    charge: i32,
    spin: f64,
}

impl Element {
    fn new(mass: f64, charge: i32, spin: f64) -> Element {
        Element { mass, charge, spin }
    }
}

trait Wavefunction {
    fn wavefunction(&self, x: f64, y: f64, z: f64) -> f64;
}

/*
 Cheat: the maths of the deal
 Neutron: ψ(x, y, z) = Ae^(-r^2/2σ^2)
 Oxygen: Ψ = Ψ(x1, y1, z1, x2, y2, z2, ..., xN, yN, zN)
 Hydrogen: Ψ(r, θ, φ) = R(r) * Y(θ, φ)
 Carbon: Ψ(x, y, z) = Σc_ij * φ_j(x, y, z)
*/

struct Carbon {}
impl Carbon {
    fn new() -> Carbon {
        Carbon {}
    }
}

impl Element for Carbon {
    fn new() -> Element {
        Element::new(12.0, 6, 0.5)
    }
}

impl Wavefunction for Carbon {
    fn wavefunction(&self, x: f64, y: f64, z: f64) -> f64 {
        (1.0 / 3.0).sqrt() * (2.0 * PI * x).cos() + (PI * y).cos() + (PI * z).cos()
    }
}

struct Hydrogen {}
impl Hydrogen {
    fn new() -> Hydrogen {
        Hydrogen {}
    }
}

impl Element for Hydrogen {
    fn new() -> Element {
        Element::new(1.0, 1, 0.5)
    }
}

impl Wavefunction for Hydrogen {
    fn wavefunction(&self, x: f64, y: f64, z: f64) -> f64 {
        (1.0 / PI).sqrt() * ((x.powi(2) + y.powi(2) + z.powi(2)).sqrt() * -1.0).exp()
    }
}

struct Oxygen {}
impl Oxygen {
    fn new() -> Oxygen {
        Oxygen {}
    }
}

impl Element for Oxygen {
    fn new() -> Element {
        Element::new(16.0, 8, 0.5)
    }
}

impl Wavefunction for Oxygen {
    fn wavefunction(&self, x: f64, y: f64, z: f64) -> f64 {
        (1.0 / 5.0).sqrt() * (2.0 * PI * x).cos() + (2.0 * PI * y).cos() - (PI * z).cos()
    }
}

struct Neutron {}
impl Neutron {
    fn new() -> Neutron {
        Neutron {}
    }
}

impl Element for Neutron {
    fn new() -> Element {
        Element::new(1.00866491595, 0, 0.5)
    }
}

impl Wavefunction for Neutron {
    fn wavefunction(&self, x: f64, y: f64, z: f64) -> f64 {
        (1.0 / ((2.0 * PI).sqrt() * 0.67)) * ((x.powi(2) + y.powi(2) + z.powi(2)) / (0.67.powi(2) * -0.5)).exp()
    }
}

fn sintetizar_deoxirribose() -> Vec<(Atom, i32)> {
    // Perform enzymatic steps to synthesize deoxyribose
    let ribose = vec![(Atom::Carbon, 5), (Atom::Hydrogen, 10), (Atom::Oxygen, 5)]; // Bio formula for C5-H10-O5
    let enzimas = vec![
        vec![(Atom::Carbon, 2), (Atom::Hydrogen, 3), (Atom::Oxygen, 2)],
        vec![(Atom::Oxygen, 1), (Atom::Hydrogen, 1)],
        vec![(Atom::Hydrogen, 1), (Atom::Oxygen, 1)]
    ]; // C2H3O2-OH-HO
    // Each enzyme is represented as a vector of tuples, indicating the atoms it contains and their number
    for enzima in enzimas {
        for (atom, num) in enzima {
            for _ in 0..num {
                ribose.push((atom, 1)); // Add the atoms from the enzyme to the ribose molecule
            }
        }
    }
    return vec![(Atom::Carbon, 5), (Atom::Hydrogen, 10), (Atom::Oxygen, 4)] + &ribose; // Return the completed deoxyribose molecule with one less oxygen atom
}


fn sintetizar_adenina() -> Vec<(Element, i32)> {
    // Perform enzymatic steps to synthesize adenine
    let precursores = vec![
        vec![(Carbon::new(), 5), (Hydrogen::new(), 5), (Neutron::new(), 1)],
        vec![(Carbon::new(), 4), (Hydrogen::new(), 5), (Neutron::new(), 1)],
    ];
    let enzimas = vec![
        vec![
            (Carbon::new(), 2),
            (Hydrogen::new(), 3),
            (Neutron::new(), 1),
            (Oxygen::new(), 1),
        ],
        vec![(Carbon::new(), 1), (Hydrogen::new(), 3), (Neutron::new(), 1)],
    ]; // C2H3N1O1-CHN
    // Each enzyme is represented as a vector of tuples, indicating the atoms it contains and their number
    let mut adenine = Vec::new();
    for precursor in precursores {
        for enzyme in enzimas.iter() {
            for (atom, num) in enzyme.iter() {
                for _i in 0..*num {
                    adenine.push((*atom, 1)); // Add the atoms from the enzyme to the adenine molecule
                }
            }
            for (atom, num) in precursor.iter() {
                for _i in 0..*num {
                    adenine.push((*atom, 1)); // Add the atoms from the precursor to the adenine molecule
                }
            }
        }
    }
    return adenine;
}

fn sintetizar_citosina() -> Vec<(Elemento, i32)> {
    // Perform enzymatic steps to synthesize cytosine
    let mut precursores = vec![        vec![(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 1)],
        vec![(Carbon(), 4), (Hydrogen(), 4), (Neutron(), 2)],
    ];
    let enzimas = vec![        vec![(Carbon(), 3), (Hydrogen(), 2), (Oxygen(), 1)],
        vec![(Carbon(), 2), (Oxygen(), 1), (Hydrogen(), 3), (Neutron(), 1)],
        vec![(Carbon(), 3), (Hydrogen(), 3), (Neutron(), 1)],
    ];
    // Each enzyme is represented as a vector of tuples, indicating the atoms it contains and their number
    for precursor in precursores.iter_mut() {
        for enzima in enzimas.iter() {
            for (atom, num) in enzima.iter() {
                for _i in 0..*num {
                    precursor.push((*atom, 1)); // Add the atoms from the enzyme to the precursor molecule
                }
            }
        }
    }
    return vec![(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 3)] + precursores; // Return the completed cytosine molecule
}

fn sintetizar_guanina() -> Vec<(Elemento, i32)> {
    // Perform enzymatic steps to synthesize guanine
    let mut precursores = vec![        vec![(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 1)],
        vec![(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 3)],
    ];
    let enzimas = vec![        vec![(Carbon(), 4), (Hydrogen(), 4), (Neutron(), 1)],
        vec![(Carbon(), 2), (Hydrogen(), 3), (Neutron(), 3)],
        vec![(Carbon(), 2), (Oxygen(), 1), (Hydrogen(), 3), (Neutron(), 1)],
    ];
    // Each enzyme is represented as a vector of tuples, indicating the atoms it contains and their number
    for precursor in precursores.iter_mut() {
        for enzima in enzimas.iter() {
            for (atom, num) in enzima.iter() {
                for _i in 0..*num {
                    precursor.push((*atom, 1)); // Add the atoms from the enzyme to the precursor molecule
                }
            }
        }
    }
    return vec![(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 5)] + precursores; // Return the completed guanine molecule
}

fn sintetizar_timina() -> Vec<(Atom, i32)> {
    // Perform enzymatic steps to synthesize thymine
    let mut precursores = vec![
        vec![(Atom::Carbon, 4), (Atom::Hydrogen, 5), (Atom::Neutron, 1)],
        vec![(Atom::Carbon, 2), (Atom::Hydrogen, 4), (Atom::Oxygen, 2)],
        vec![(Atom::Carbon, 2), (Atom::Hydrogen, 3), (Atom::Neutron, 1)],
    ];
    let enzimas = vec![
        vec![(Atom::Carbon, 2), (Atom::Oxygen, 1), (Atom::Hydrogen, 3), (Atom::Neutron, 1)],
        vec![(Atom::Carbon, 4), (Atom::Hydrogen, 4), (Atom::Neutron, 2)],
        vec![(Atom::Carbon, 3), (Atom::Hydrogen, 3), (Atom::Oxygen, 1)],
    ];
    // Each enzyme is represented as a vector of tuples, indicating the atoms it contains and their number
    for precursor in precursores.iter_mut() {
        for enzima in enzimas.iter() {
            for (atom, num) in enzima.iter() {
                for _i in 0..*num {
                    precursor.push((*atom, 1)); // Add the atoms from the enzyme to the precursor molecule
                }
            }
        }
    }
    return vec![
        (Atom::Carbon, 5),
        (Atom::Hydrogen, 6),
        (Atom::Neutron, 2),
        (Atom::Oxygen, 2),
    ] + precursores.concat(); // Return the completed thymine molecule
}

/*
// Might perform better, Need to double check results consistency before
fn sintetizar_timina() -> Vec<(Atom, u8)> {
    // Perform enzymatic steps to synthesize thymine
    let mut precursores = vec![
        vec![(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 1)],
        vec![(Carbon(), 2), (Hydrogen(), 4), (Oxygen(), 2)],
        vec![(Carbon(), 2), (Hydrogen(), 3), (Neutron(), 1)]
    ];
    let enzimas = vec![
        vec![(Carbon(), 2), (Oxygen(), 1), (Hydrogen(), 3), (Neutron(), 1)],
        vec![(Carbon(), 4), (Hydrogen(), 4), (Neutron(), 2)],
        vec![(Carbon(), 3), (Hydrogen(), 3), (Oxygen(), 1)]
    ];
    for precursor in &mut precursores {
        for enzima in &enzimas {
            for &(atom, num) in enzima {
                for _ in 0..num {
                    precursor.push((atom, 1)); // Add the atoms from the enzyme to the precursor molecule
                }
            }
        }
    }
    vec![("C", 5), (Hydrogen(), 6), (Neutron(), 2), (Oxygen(), 2)].into_iter().chain(precursores.into_iter().flatten()).collect()
}
*/

fn sintetizar_nucleotideo(base: char) -> Vec<(Atom, i32)> {
    // Perform enzymatic steps to synthesize a nucleotide with the given base
    let deoxirribose = sintetizar_deoxirribose();
    let base = match base {
        'A' => sintetizar_adenina(),
        'C' => sintetizar_citosina(),
        'G' => sintetizar_guanina(),
        'T' => sintetizar_timina(),
        _ => panic!("Invalid base: must be one of A, C, G, T"),
    };
    return vec![
        (Atom::Phosphorus, 1),
        (Atom::Oxygen, 4),
    ] + deoxirribose.concat() + base.concat(); // Return the completed nucleotide molecule
}

fn sintetizar_dna(comprimento: i32) -> Vec<(Atom, i32)> {
    // Perform enzymatic steps to synthesize a DNA strand with the given length
    let mut dna = vec![];
    for _i in 0..comprimento {
        let nucleotideo = sintetizar_nucleotideo(['A', 'C', 'G', 'T'].choose(&mut rand::thread_rng()).unwrap());
        dna.append(&mut nucleotideo.clone());
    }
    return dna;
}

/*
 // Might perform better, Need to double check results consistency before
 fn sintetizar_dna(comprimento: usize) -> Vec<Vec<(Atom, u8)>> {
    let mut dna = Vec::new();
    for _ in 0..comprimento {
        let nucleotideo = sintetizar_nucleotideo(&['A', 'C', 'G', 'T'][rand::random::<usize>() % 4]);
        dna.push(nucleotideo);
    }
    dna
} */

fn main() {
    // Either read the genome sequence from a file in FASTA format
    // Or download it from https://ftp.ensemblgenomes.ebi.ac.uk/pub/protists/release-56/fasta/paramecium_tetraurelia
    let genome = fs::read_to_string("/usr/home/eksffa/phraphread/seq/3/paramecyumSequence.phrap").expect("Failed to read genome file");

    // Synthesize the DNA from the genome sequence
    let dna = sintetizar_dna(&genome);

    // Output the synthesized DNA
    println!("{:?}", dna);
}

